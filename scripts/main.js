

function watch(el){
  let iframe = document.querySelector('iframe');
  let dialog = document.querySelector('dialog');
  if (dialog.style.top!='200px'){
    iframe.src = el.getAttribute('youtube-url');
    dialog.style.top = '200px';
    dialog.style.opacity = '1';
  }
}

function closedialog(){
  let dialog = document.querySelector('dialog');
  let iframe = document.querySelector('iframe');
  if (dialog.style.top=='200px'){
    iframe.src = '';
    dialog.style.top = '-1000px';
    dialog.style.opacity = '0';
  }
}
