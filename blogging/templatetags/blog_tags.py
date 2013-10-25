from django import template
import markdown


register = template.Library()

def md_to_html(md):
    return markdown.markdown(md)
    
register.filter('md_to_html', md_to_html)
