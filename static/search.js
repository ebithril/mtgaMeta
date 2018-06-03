$(function() {
	$('button').click(function() {
		var searchString = $('#txtSearch').val();
		$.ajax({
			url: '/search',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
				var element = document.getElementById('result');
				element.innerHTML = ''
				for (i = 0; i < response.length; ++i) {
					var div = document.createElement('div');
					div.classList.add('card')

					var img = document.createElement('img');
					img.src = response[i]['image'];
					div.appendChild(img);

					var paragraph = document.createElement('p');
					var node = document.createTextNode(response[i]['name']);
					paragraph.appendChild(node);
					div.appendChild(paragraph);

					element.appendChild(div);
				}
			},
			error: function(error) {
				console.log(error);
			}
		});
	});
});
