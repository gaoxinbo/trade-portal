require.config({
    baseUrl : 'static/scripts/lib',
    paths:{
        'Vue' : 'https://unpkg.com/vue/dist/vue',
        "jquery": "https://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min"
    }
});


requirejs(['index']);