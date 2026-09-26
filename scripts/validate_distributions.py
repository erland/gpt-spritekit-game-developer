#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
KNOWLEDGE=[
 '01-GPT-ROLE-AND-PRINCIPLES.md','02-GAME-DESIGN-FOUNDATIONS.md',
 '03-INSPIRATION-AND-DIFFERENTIATION.md','04-TVOS-SPRITEKIT-ARCHITECTURE.md',
 '05-CONTROLLER-AND-TV-UX.md','06-PROJECT-ZIP-WORKFLOW.md',
 '07-TESTING-AND-RELEASE.md','08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md',
 '09-GENRE-PLATFORMER.md','10-GENRE-SHOOT-EM-UP.md',
 '11-GENRE-TURN-BASED-STRATEGY.md','12-GENRE-TOP-DOWN-ACTION.md',
 '13-GENRE-ISOMETRIC-ADVENTURE.md','14-GENRE-PUZZLE.md',
 '15-GENRE-LOCAL-MULTIPLAYER.md','16-VERSION-CONTROL-AND-CI.md'
]

def h(b):
    return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--version')
    ap.add_argument('--dist',default='dist')
    a=ap.parse_args()
    v=(a.version or (ROOT/'VERSION').read_text().strip()).removeprefix('v')

    dist=ROOT/a.dist
    registry=yaml.safe_load((ROOT/'runtime-distribution-registry.yaml').read_text(encoding='utf-8'))
    active=list(registry.get('active_targets',[]) or [])
    expected={registry['targets'][name]['artifact_pattern'].format(version=v) for name in active}
    actual={p.name for p in dist.glob('*.zip')}
    if actual!=expected:
        raise SystemExit(f'Distribution set mismatch. expected={sorted(expected)} actual={sorted(actual)}')

    cz=dist/f'spritekit-developer-custom-gpt-v{v}.zip'
    pz=dist/f'spritekit-developer-chat-v{v}.zip'
    for z in [p for p in (cz,pz) if p.name in expected]:
        with zipfile.ZipFile(z) as q:
            if q.testzip():
                raise SystemExit(f'Corrupt zip: {z}')

    canonical=(ROOT/'assistant/instructions.md').read_bytes()
    starters=(ROOT/'config/CONVERSATION-STARTERS.md').read_bytes()
    critical=[
        'tvOS är produktplattform',
        'macOS är officiell utvecklings- och testplattform',
        'Den senaste kompletta åtkomliga projektzippen är sanningskällan.',
        'Säkerhetsgranska arkivvägar mot zip-slip/path traversal',
        'ändra aldrig originalarkivet',
        'Påstå aldrig att något är byggt, testat eller verifierat om det inte är det.',
    ]

    if 'custom-gpt' in active:
        with zipfile.ZipFile(cz) as z:
            custom_instr=z.read('config/FINAL-INSTRUCTIONS.md')
            assert custom_instr==canonical
            for marker in critical:
                assert marker in custom_instr.decode('utf-8'), f'Custom GPT missing behavior marker: {marker}'
            assert z.read('config/CONVERSATION-STARTERS.md')==starters
            for n in KNOWLEDGE:
                assert z.read('knowledge/'+n)==(ROOT/'knowledge'/n).read_bytes()
            assert z.read('VERSION').decode().strip()==v

    if 'chat' in active:
        with zipfile.ZipFile(pz) as z:
            chat_instr=z.read('assistant/instructions.md')
            assert chat_instr==canonical
            for marker in critical:
                assert marker in chat_instr.decode('utf-8'), f'Chat missing behavior marker: {marker}'
            assert z.read('assistant/conversation-starters.md')==starters
            for n in KNOWLEDGE:
                assert z.read('knowledge/'+n)==(ROOT/'knowledge'/n).read_bytes()
            assert z.read('VERSION').decode().strip()==v
            m=json.loads(z.read('MANIFEST.json'))
            assert m['version']==v
            for name,expected_hash in m['sha256'].items():
                assert h(z.read(name))==expected_hash, name

    print(f'OK: distributions validated for {v}')

if __name__=='__main__':
    main()
