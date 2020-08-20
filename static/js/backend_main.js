if (__page__ == 'home' || __page__ == 'category'){

var first = true
var current_page = 1
var all_pages_loaded = []
var pagination_data = {}

if (__page__ == 'home'){
    var url = 'api/home/'
}else{
    var url = '../api/category/' + category
}

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


function load_posts(){
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
        div_.id = 'home_page_entries1'
        div_.classList.add('entries')

        if (first){
            first = false
            if (data['results'].length == 0){
                document.getElementById('main___').innerHTML += ('<p>No Posts</p>')
            }
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

        
        paginate(data)
        push_page(1)//Its our first page and since we have loaded it , add it to loaded_pages
        
    
    })
}


function shift_page(page){
    if (all_pages_loaded.includes(page)){
        //Then we have the posts;so no need to to load_again
       display_page(page)
    }
    else{
        
        //We have not loaded the page so load the page
        
        t_url = url + '?page=' + page

        fetch(t_url,{
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
            next = data['next']
            previous = data['previous']
            var div_ =  document.createElement('div')
            div_.style.display = 'none'
            div_.id = 'home_page_entries'+page
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
            var divs = document.getElementsByClassName('entries')
            for (let i = 0; i < divs.length; i++){
        
                divs[i].style.display = 'none' //Hide all pages
        
            }
            div_.style.removeProperty('display')
            document.getElementById('main___').appendChild(div_) 

            paginate(data)
            push_page(page) //We loaded this page to loaded pages
            }
        )
    }
}
    

function display_page(page){

    var divs = document.getElementsByClassName('entries')
    for (let i = 0; i < divs.length; i++){

        divs[i].style.display = 'none' //Hide all pages

    }

    document.getElementById('home_page_entries'+page).style.removeProperty('display') //Now only display the page requested
    paginate(null,false,page)
}

function push_page(page){
    all_pages_loaded.push(page)
}


function paginate(data=null,new_page=true,page=null){

    if (! new_page){

        var paginator_obj =  pagination_data[page]
        var pages_back = paginator_obj['pages_back']
        var pages_forth = paginator_obj['pages_forth']
        var c_page = paginator_obj['current_page']

    } else {
        var paginator_obj = data['paginator']
        var pages_back = paginator_obj['pages_back']
        var pages_forth = paginator_obj['pages_forth']
        var c_page = paginator_obj['current_page']

        //Since for the next time we will not load this page, save the data -- pagination data
        pagination_data[c_page] = {
            'pages_back':pages_back,
            'pages_forth':pages_forth,
            'current_page':c_page,
        }
    }

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

