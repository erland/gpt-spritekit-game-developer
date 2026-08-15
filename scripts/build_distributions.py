#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = [
    '01-GPT-ROLE-AND-PRINCIPLES.md','02-GAME-DESIGN-FOUNDATIONS.md',
    '03-INSPIRATION-AND-DIFFERENTIATION.md','04-TVOS-SPRITEKIT-ARCHITECTURE.md',
    '05-CONTROLLER-AND-TV-UX.md','06-PROJECT-ZIP-WORKFLOW.md',
    '07-TESTING-AND-RELEASE.md','08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md',
    '09-GENRE-PLATFORMER.md','10-GENRE-SHOOT-EM-UP.md',
    '11-GENRE-TURN-BASED-STRATEGY.md','12-GENRE-TOP-DOWN-ACTION.md',
    '13-GENRE-ISOMETRIC-ADVENTURE.md','14-GENRE-PUZZLE.md',
    '15-GENRE-LOCAL-MULTIPLAYER.md','16-VERSION-CONTROL-AND-CI.md',
]
SEMVER = re.compile(r'^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')
FIXED_DT=(2020,1,1,0,0,0)

def version(v):
    v = v or (ROOT/'VERSION').read_text(encoding='utf-8').strip()
    if v.startswith('v'): v=v[1:]
    if not SEMVER.fullmatch(v): raise SystemExit(f'Invalid version: {v}')
    return v

def write_zip(src: Path, dest: Path):
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(x for x in src.rglob('*') if x.is_file()):
            info=zipfile.ZipInfo(p.relative_to(src).as_posix(), FIXED_DT)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=(0o644 & 0xFFFF) << 16
            z.writestr(info,p.read_bytes())

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--output-dir',default='dist'); a=ap.parse_args()
    v=version(a.version); out=ROOT/a.output_dir; shutil.rmtree(out,ignore_errors=True); out.mkdir(parents=True)
    tmp=out/'.build'; custom=tmp/'custom'; chat=tmp/'chat'
    for d in (custom,chat): d.mkdir(parents=True)
    # Custom GPT package: preserve canonical builder inputs byte-for-byte.
    (custom/'config').mkdir(); (custom/'knowledge').mkdir()
    for n in ['FINAL-INSTRUCTIONS.md','CONVERSATION-STARTERS.md','GPT-CONFIGURATION.md','BUILDER-CHECKLIST.md','KNOWLEDGE-UPLOAD-MANIFEST.md','CAPABILITIES.md']:
        shutil.copy2(ROOT/'config'/n, custom/'config'/n)
    for n in KNOWLEDGE: shutil.copy2(ROOT/'knowledge'/n, custom/'knowledge'/n)
    (custom/'VERSION').write_text(v+'\n',encoding='utf-8')
    # Portable package.
    (chat/'assistant').mkdir(); (chat/'knowledge').mkdir()
    shutil.copy2(ROOT/'portable/START-HERE.md',chat/'START-HERE.md')
    shutil.copy2(ROOT/'config/FINAL-INSTRUCTIONS.md',chat/'assistant/instructions.md')
    shutil.copy2(ROOT/'config/CONVERSATION-STARTERS.md',chat/'assistant/conversation-starters.md')
    for n in KNOWLEDGE: shutil.copy2(ROOT/'knowledge'/n,chat/'knowledge'/n)
    (chat/'VERSION').write_text(v+'\n',encoding='utf-8')
    manifest={'package':'spritekit-game-designer-developer','format':'portable-chat-assistant','version':v,'entrypoint':'START-HERE.md','instructions':'assistant/instructions.md','conversation_starters':'assistant/conversation-starters.md','knowledge':[f'knowledge/{n}' for n in KNOWLEDGE]}
    files={}
    for p in sorted(x for x in chat.rglob('*') if x.is_file() and x.name!='MANIFEST.json'):
        files[p.relative_to(chat).as_posix()]=sha(p)
    manifest['sha256']=files
    (chat/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    cz=out/f'spritekit-developer-custom-gpt-v{v}.zip'; pz=out/f'spritekit-developer-chat-v{v}.zip'
    write_zip(custom,cz); write_zip(chat,pz); shutil.rmtree(tmp)
    print(cz); print(pz)
if __name__=='__main__': main()
