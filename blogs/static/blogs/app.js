    $(document).ready(function(){
        $('a[rel="gallery"]').fancybox({
         'transitionIn': 'elastic',
         'transitionOut': 'elastic',
         'margin':40,
         'easingIn':'swing',
         'easingOut':'swing',
         'titleShow':'true',
         'title':'{{ image.image_title }}',
        
        });
        
    });
