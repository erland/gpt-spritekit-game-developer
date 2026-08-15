#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
KNOWLEDGE=['01-GPT-ROLE-AND-PRINCIPLES.md','02-GAME-DESIGN-FOUNDATIONS.md','03-INSPIRATION-AND-DIFFERENTIATION.md','04-TVOS-SPRITEKIT-ARCHITECTURE.md','05-CONTROLLER-AND-TV-UX.md','06-PROJECT-ZIP-WORKFLOW.md','07-TESTING-AND-RELEASE.md','08-GAME-ASSET-REQUIREMENTS-AND-INTEGRATION.md','09-GENRE-PLATFORMER.md','10-GENRE-SHOOT-EM-UP.md','11-GENRE-TURN-BASED-STRATEGY.md','12-GENRE-TOP-DOWN-ACTION.md','13-GENRE-ISOMETRIC-ADVENTURE.md','14-GENRE-PUZZLE.md','15-GENRE-LOCAL-MULTIPLAYER.md','16-VERSION-CONTROL-AND-CI.md']
def h(b): return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--dist',default='dist'); a=ap.parse_args(); v=(a.version or (ROOT/'VERSION').read_text().strip()).removeprefix('v')
 dist=ROOT/a.dist; cz=dist/f'spritekit-developer-custom-gpt-v{v}.zip'; pz=dist/f'spritekit-developer-chat-v{v}.zip'
 for z in (cz,pz):
  if not z.exists(): raise SystemExit(f'Missing {z}')
  with zipfile.ZipFile(z) as q:
   if q.testzip(): raise SystemExit(f'Corrupt zip: {z}')
 with zipfile.ZipFile(cz) as z:
  assert z.read('config/FINAL-INSTRUCTIONS.md')==(ROOT/'config/FINAL-INSTRUCTIONS.md').read_bytes()
  assert z.read('config/CONVERSATION-STARTERS.md')==(ROOT/'config/CONVERSATION-STARTERS.md').read_bytes()
  for n in KNOWLEDGE: assert z.read('knowledge/'+n)==(ROOT/'knowledge'/n).read_bytes()
  assert z.read('VERSION').decode().strip()==v
 with zipfile.ZipFile(pz) as z:
  assert z.read('assistant/instructions.md')==(ROOT/'config/FINAL-INSTRUCTIONS.md').read_bytes()
  assert z.read('assistant/conversation-starters.md')==(ROOT/'config/CONVERSATION-STARTERS.md').read_bytes()
  for n in KNOWLEDGE: assert z.read('knowledge/'+n)==(ROOT/'knowledge'/n).read_bytes()
  assert z.read('VERSION').decode().strip()==v
  m=json.loads(z.read('MANIFEST.json')); assert m['version']==v
  for name,expected in m['sha256'].items(): assert h(z.read(name))==expected, name
 print(f'OK: distributions validated for {v}')
if __name__=='__main__': main()
