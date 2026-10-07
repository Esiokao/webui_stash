// Personally Recommend To Do Auto Injection With TamperMonkey
// Iterate through all iframes
for (let i = 0; i < top.frames.length; i++) {
  const iframe = top.frames[i]

  try {
    // Check if iframe is from same origin
    if (iframe.location.origin === window.location.origin) {
      // Execute JavaScript within the iframe context
      // Do Injection
      iframe.eval(`
        document.addEventListener('contextmenu', function (event) {
          //   event.preventDefault();
          const element = event.target;
          const selector = getUniqueSelector(element);
          showToast(window,"✅   "+ selector)
          console.log(selector);
          _selector = '"'+selector+'"' // wrap into double quote, ctrl + v ready
          copyToClipboard(_selector);
        });

        function getUniqueSelector(el) {
          if (!(el instanceof Element)) return '';
          const path = [];
          while (el) {
            let selector = el.nodeName.toLowerCase();
            if (el.id) {
              selector = '#' + el.id;
              path.unshift(selector);
              break;
            } else {
              let sib = el,
                  nth = 1;
              while (sib.previousElementSibling) {
                sib = sib.previousElementSibling;
                if (sib.nodeName.toLowerCase() === selector) nth++;
              }
              if (nth !== 1) selector += ':nth-child(' + nth + ')';
            }
            path.unshift(selector);
            el = el.parentElement;
          }
          return path.join(' > ');
        }

        // Copy text to clipboard
        function copyToClipboard(text) {
          if (navigator.clipboard) {
            navigator.clipboard.writeText(text).catch(err =>
              console.error('❌ Clipboard API error:', err)
            )
          } else {
            const textarea = document.createElement('textarea')
            textarea.value = text
            textarea.style.position = 'fixed'
            document.body.appendChild(textarea)
            textarea.focus()
            textarea.select()
            try {
              document.execCommand('copy')
            } catch (err) {
              console.error('❌ Fallback copy error:', err)
            }
            document.body.removeChild(textarea)
          }
        }

        function showToast(win, msg) {
            const doc = win.document
            const toast = doc.createElement('div')
            toast.textContent = msg
            toast.style.position = 'fixed'
            toast.style.top = '10px'
            toast.style.left = '50%'
            toast.style.transform = 'translateX(-50%)'
            toast.style.background = '#333'
            toast.style.color = '#fff'
            toast.style.padding = '8px 16px'
            toast.style.borderRadius = '6px'
            toast.style.fontSize = '14px'
            toast.style.zIndex = '9999'
            toast.style.opacity = '0'
            toast.style.transition = 'opacity 0.3s ease'
            doc.body.appendChild(toast)

            requestAnimationFrame(() => {
                toast.style.opacity = '1'
            })

            setTimeout(() => {
                toast.style.opacity = '0'
                toast.addEventListener('transitionend', () => {
                    doc.body.removeChild(toast)
                })
            }, 2000)
        }

      `)
    }
  } catch (e) {
    console.warn(`⚠️ Cannot access iframe: ${iframe.location.href}`, e)
  }
}
