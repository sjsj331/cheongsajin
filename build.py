# Inline vendored three.js (r158, MIT) into src.html -> index.html (single self-contained file)
s=open('src.html').read()
t=open('three.min.js').read().replace('</script','<\\/script')
open('index.html','w').write(s.replace('/*__THREE__*/', t))
