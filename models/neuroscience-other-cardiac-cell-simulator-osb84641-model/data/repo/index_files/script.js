function popup(text, url) {
	check = confirm(text);
	if (check == true) {
		window.location.href = url;
	} else {
	}
}