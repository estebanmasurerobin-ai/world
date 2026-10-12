W="M 262 282 L 387 628 L 512 362 L 637 628 L 762 282"
U="M 236 760 L 788 760"
def svg(mode,size=1024):
    d=mode!='light'; t=mode=='tinted'
    b1,b2=('#ffffff','#f1f3f6') if not d else ('#1a1a1c','#000000')
    c1,c2=('#f2f2f2','#b4b4b4') if t else (('#b9c6d8','#8193ad') if not d else ('#b9c6d8','#8193ad'))
    w1,w2=('#3a3a3e','#0b0b0d') if mode=='light' else (('#ffffff','#d0d0d0') if t else ('#ffffff','#e6e8ec'))
    rim='rgba(255,255,255,.75)' if not d else 'rgba(255,255,255,.55)'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 1024 1024">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{b1}"/><stop offset="1" stop-color="{b2}"/></linearGradient>
<linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="250" x2="0" y2="790"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="gw" gradientUnits="userSpaceOnUse" x1="0" y1="250" x2="0" y2="700"><stop offset="0" stop-color="{w1}"/><stop offset="1" stop-color="{w2}"/></linearGradient>
<filter id="hil" x="-20%" y="-20%" width="140%" height="140%"><feMorphology in="SourceAlpha" operator="erode" radius="4" result="e"/><feOffset in="e" dx="0" dy="5" result="o"/><feComposite in="SourceGraphic" in2="o" operator="out"/></filter>
<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="18"/></filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
 <path d="{W}" stroke="{'rgba(0,0,0,.35)' if d else 'rgba(60,80,110,.16)'}" stroke-width="96" filter="url(#sh)" transform="translate(0 18)"/>
 <path d="{U}" stroke="{'rgba(0,0,0,.35)' if d else 'rgba(60,80,110,.16)'}" stroke-width="44" filter="url(#sh)" transform="translate(0 18)"/>
 <path d="{W}" stroke="url(#gw)" stroke-width="96"/>
 <path d="{U}" stroke="url(#g)" stroke-width="44"/>
 <path d="{W}" stroke="{rim if d else 'rgba(255,255,255,.22)'}" stroke-width="96" filter="url(#hil)"/>
 <path d="{U}" stroke="{rim}" stroke-width="44" filter="url(#hil)"/>
</g>
</svg>'''
if __name__=='__main__':
    for m in ('light','dark','tinted'): open(f'x_{m}.svg','w').write(svg(m))
