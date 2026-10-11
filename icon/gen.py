import sys
def svg(mode, size=1024, bg=True):
    dark = mode=='dark'
    if dark:
        bg1,bg2='#151a2e','#05060c'; blobs=[('#3b5bff',330,300,330,.55),('#b04dff',720,760,300,.45),('#00c2ff',780,260,220,.35)]
        body1,body2='rgba(255,255,255,.20)','rgba(255,255,255,.04)'; rim1,rim2='rgba(255,255,255,.95)','rgba(255,255,255,.12)'
        barb='rgba(255,255,255,.22)'; shaft='rgba(255,255,255,.85)'; shadow='rgba(0,0,0,.6)'; nib1,nib2='#e9ecff','#8d97c9'
    else:
        bg1,bg2='#ffffff','#e4e9f7'; blobs=[('#5b8cff',330,300,330,.42),('#c77dff',720,760,300,.38),('#36d1ff',790,250,220,.30)]
        body1,body2='rgba(255,255,255,.62)','rgba(120,140,255,.22)'; rim1,rim2='rgba(255,255,255,1)','rgba(255,255,255,.35)'
        barb='rgba(255,255,255,.75)'; shaft='rgba(60,75,140,.55)'; shadow='rgba(40,60,130,.28)'; nib1,nib2='#5a6798','#1d2440'
    blobsvg=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{o}"/>' for c,x,y,r,o in blobs)
    # Plume dans un repère vertical (tige sur x=0), tournée ensuite de 38°
    vane=("M 2 170 C -40 150 -88 70 -98 -40 L -76 -52 L -102 -92 C -110 -200 -74 -320 6 -420 "
          "C 44 -360 80 -280 86 -196 L 64 -184 L 90 -150 C 94 -60 74 50 42 112 L 26 104 L 30 138 C 22 152 12 164 2 170 Z")
    barbs=''.join(f'<path d="M {0.0:.0f} {y} Q -40 {y-10} -150 {y-90}" />' for y in range(150,-420,-44)) + \
          ''.join(f'<path d="M 2 {y} Q 40 {y-12} 150 {y-96}" />' for y in range(128,-420,-44))
    bgrect = f'''<rect width="1024" height="1024" fill="url(#bg)"/><g filter="url(#blur)">{blobsvg}</g>''' if bg else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 1024 1024">
<defs>
 <radialGradient id="bg" cx="30%" cy="20%" r="95%"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></radialGradient>
 <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="90"/></filter>
 <filter id="refr" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/><feColorMatrix type="saturate" values="1.8"/></filter>
 <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter>
 <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
 <linearGradient id="body" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{body1}"/><stop offset="1" stop-color="{body2}"/></linearGradient>
 <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{rim1}"/><stop offset=".5" stop-color="{rim2}"/><stop offset="1" stop-color="{rim1}"/></linearGradient>
 <linearGradient id="nib" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{nib1}"/><stop offset="1" stop-color="{nib2}"/></linearGradient>
 <clipPath id="vclip"><path d="{vane}"/></clipPath>
</defs>
{bgrect}
<g transform="translate(530 540) rotate(40) scale(1.22)">
 <path d="{vane}" fill="{shadow}" filter="url(#shadow)" transform="translate(-18 34)"/>
 <path d="M -7 170 L 7 170 L 6 320 L -6 320 Z" opacity=".5" fill="{shadow}" filter="url(#shadow)" transform="translate(-18 34)"/>
 <g clip-path="url(#vclip)">
  <g transform="rotate(-40) translate(-530 -540) translate(30 -20)" filter="url(#refr)">{blobsvg}</g>
  <path d="{vane}" fill="url(#body)"/>
  <g stroke="{barb}" stroke-width="3" fill="none" stroke-linecap="round">{barbs}</g>
  <path d="M -88 -20 C -98 -150 -70 -280 -6 -380" stroke="#fff" stroke-opacity="{'.55' if dark else '.95'}" stroke-width="12" fill="none" stroke-linecap="round" filter="url(#soft)"/>
 </g>
 <path d="{vane}" fill="none" stroke="{'rgba(0,0,0,0)' if dark else 'rgba(70,90,170,.35)'}" stroke-width="9"/>
 <path d="{vane}" fill="none" stroke="url(#rim)" stroke-width="5"/>
 <path d="M 6 -416 Q -8 -130 2 170" stroke="{shaft}" stroke-width="7" fill="none" stroke-linecap="round"/>
 <!-- tuyau et bec -->
 <path d="M -8 168 L 8 168 L 8 262 C 8 290 3 310 0 336 C -3 310 -8 290 -8 262 Z" fill="url(#nib)"/>
 <path d="M -3 176 L -3 262" stroke="#fff" stroke-opacity=".6" stroke-width="3" stroke-linecap="round"/>
 <path d="M 0 280 L 0 318" stroke="{bg2 if not dark else '#05060c'}" stroke-width="2"/>
</g>
</svg>'''
for m in ('light','dark'):
    open(f'{m}.svg','w').write(svg(m))
open('dark-nobg.svg','w').write(svg('dark',bg=False))

import re
def pref(t,p): return re.sub(r'url\(#(\w+)\)', lambda m: f'url(#{p}{m.group(1)})', re.sub(r'id="(\w+)"', lambda m: f'id="{p}{m.group(1)}"', t))
inner=lambda m,p: pref(re.sub(r'^<svg[^>]*>|</svg>$','',svg(m).strip()),p)
open('favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><style>.d{display:none}@media (prefers-color-scheme:dark){.l{display:none}.d{display:inline}}</style><g class="l">'+inner('light','l')+'</g><g class="d">'+inner('dark','d')+'</g></svg>')
