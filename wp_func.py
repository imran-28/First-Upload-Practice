def wp_post(content):
    code = f'<!-- wp:paragraph --><p>{content}</p><!-- /wp:paragraph -->'
    return code

def heading_two(h2):
    code = f'<!-- wp:heading --><h2 class="wp-block-heading">{h2}</h2><!-- /wp:heading -->'
    return code