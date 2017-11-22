function ajaxRequest(url, method, handler) {
	var url =  item.dataset.url;
	var req = new XMLHttpRequest();
	req.open("POST", url);
	req.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'));
	req.onreadystatechange = handler;
	req.send();
}