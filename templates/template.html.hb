<html>

<head>
    <link rel="stylesheet" href="./css/phb.standalone.css">
</head>

<body>
    {{#each pages}}
    <div class="phb">
        {{ content }}
        <div class='footnote'>{{ title }}</div>
        <div class='pageNumber auto'></div>
    </div>
    <br/>
    {{/each}}
</body>

</html>
