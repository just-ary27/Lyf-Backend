anime({
    targets: '#lines path',
        strokeDashoffset: [anime.setDashoffset, 0],
        easing: 'easeInOutSine',
        duration: 5000,
        delay: function(el, i) { return i * 250 },
        direction: 'alternate',
        loop: true
      });
anime({
    targets: '#brokenlines path',
        strokeDashoffset: [anime.setDashoffset, 0],
        easing: 'easeInOutSine',
        duration: 8000,
        delay: function(el, i) { return i * 150 },
        direction: 'alternate',
        loop: true
       });
    
