     const items = localStorage.getItem('appended'); // получили по ключу свой элемент
    var elements = JSON.parse(items) || []; // распарсили полученный элемент
    // пройдем по элементам и добавим их к body
    for (var index = 0; index < elements.length; index++) {
       $('body').append(elements[index]); // дабавили к body наш элемент
    }

