if (__page__ == 'search'){
    var first = true
    var current_page = 1
    var sq_ = __search_and_filter__ 

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');


    function get_url(page=current_page){

        return '../search/api?' + sq_ + '&page=' + page

    }

    function load_posts(){

        url = get_url()

        fetch(url,{
            method:'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            }
        })
        .then((resp)=>{
            return resp.json()
        })
        .then((data)=>{
            
            var div_ =  document.createElement('div')
            div_.style.display = 'none'
            div_.classList.add('entries')
            if (first){
                var paginate__ = true
                if (data['results'].length == 0){
                    document.getElementById('main___').innerHTML += ('<h1 class="text-center">No Posts</h1>')
                    var paginate__ = false
                }
                first = false
            }
            for (post of data['results'] ){
    
                post_title = post['title']
                post_slug = post['slug']
                post_cat = post['catogory']
                post_posted = post['posted'].split('T')[0]
                post_img = post['thumbnail']
    
                item = ('<article class="col-block"><div class="item-entry" data-aos="zoom-in"><div class="item-entry__thumb"><a href="single-standard.html" class="item-entry__thumb-link"><img src="' + post_img + '" alt=""></a></div><div class="item-entry__text"><div class="item-entry__cat"><a href="category.html">'+ post_cat +'</a></div><h1 class="item-entry__title"><a href="single-standard.html">'+ post_title +'</a></h1><div class="item-entry__date"><a href="single-standard.html">'+ post_posted +'</a></div></div></div></article>')
                div_.innerHTML += item
    
            }

            div_.style.removeProperty('display')
            document.getElementById('main___').appendChild(div_) 

            if (paginate__){
                paginate(data)
            }

        })
    }

    function shift_page(page){
            
        url = get_url(page)

        fetch(url,{
            method:'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            }  
        })
        .then((resp)=>{
            return resp.json()
        })
        .then((data)=>{

            var div_ =  document.createElement('div')
            div_.style.display = 'none'
            div_.classList.add('entries')
            for (post of data['results'] ){

                post_title = post['title']
                post_slug = post['slug']
                post_cat = post['catogory']
                post_posted = post['posted'].split('T')[0]
                post_img = post['thumbnail']

                item = ('<article class="col-block"><div class="item-entry" data-aos="zoom-in"><div class="item-entry__thumb"><a href="single-standard.html" class="item-entry__thumb-link"><img src="' + post_img + '" alt=""></a></div><div class="item-entry__text"><div class="item-entry__cat"><a href="category.html">'+ post_cat +'</a></div><h1 class="item-entry__title"><a href="single-standard.html">'+ post_title +'</a></h1><div class="item-entry__date"><a href="single-standard.html">'+ post_posted +'</a></div></div></div></article>')
                div_.innerHTML += item

            }
    
            div_.style.removeProperty('display')
            document.getElementById('main___').innerHTML = ''
            document.getElementById('main___').appendChild(div_) 

            paginate(data)
            }
        )
        
    }


    function paginate(data){

  
        var paginator_obj = data['paginator']
        var pages_back = paginator_obj['pages_back']
        var pages_forth = paginator_obj['pages_forth']
        var c_page = paginator_obj['current_page']


        var ul = document.createElement('ul')

        for (let i = 0 ; i < pages_back.length; i++){

            var page_ = pages_back[i]

            ul.id = 'paginator_ul'

            var li = document.createElement('li')
            var a = document.createElement('a')
            a.classList.add('pgn__num')
            a.text = page_

            a.setAttribute('onclick','shift_page(' + page_ +')')
            
            li.appendChild(a)
            ul.appendChild(li)

        }

        ul.id = 'paginator_ul'

        var li = document.createElement('li')
        var a = document.createElement('a')
        a.classList.add('pgn__num')
        a.text = c_page
        a.classList.add('current')

        a.setAttribute('onclick','shift_page(' + page_ +')')

        li.appendChild(a)
        ul.appendChild(li)

        for (let i = 0 ; i < pages_forth.length; i++){

            var page_ = pages_forth[i]


            ul.id = 'paginator_ul'

            var li = document.createElement('li')
            var a = document.createElement('a')
            a.classList.add('pgn__num')
            a.text = page_

            a.setAttribute('onclick','shift_page(' + page_ +')')
            
            li.appendChild(a)
            ul.appendChild(li)

        }

        document.getElementById('paginator__').innerHTML = ''
        document.getElementById('paginator__').appendChild(ul)
    }

}