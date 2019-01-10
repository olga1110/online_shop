  $(function () {
      $('.jcarousel').jcarousel({
        // Configuration goes here
        animation: {
          duration: 900,
          easing: 'linear',
          complete: function () {}
        },
        wrap: 'circular'
      })
    })

    $('.jcarousel').jcarouselAutoscroll({
      interval: 3000,
      target: '+=1',
      autostart: true
    })

    })


