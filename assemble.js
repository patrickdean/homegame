const glob = require('glob');
const fm = require('front-matter');
const fs = require('fs');
const marked = require('marked');
const Handlebars = require('handlebars');
const beautify_html = require('js-beautify').html;

files = glob.sync('./sections/*.md');

let contents = [];

for (let file of files) {
    let content = fm(fs.readFileSync(file, { encoding: 'utf8', flag: 'r' }));

    if (content.attributes.order) {
        let pages = content.body.split("\\page");
        for (let page of pages) {
            let html = new Handlebars.SafeString(marked(page));
            contents.push({ title: content.attributes.title, content: html });
        }
    }
}

const templateFile = fs.readFileSync('./templates/template.html.hbs', { encoding: 'utf8', flag: 'r' });
const template = Handlebars.compile(templateFile);
const render = beautify_html(template({ pages: contents }));

fs.writeFileSync('./dist/index.html', render, { encoding: 'utf8' });
