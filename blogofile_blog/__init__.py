#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import blogofile
import blogofile.plugin
from blogofile.cache import bf, HierarchicalCache as HC

## Configure the plugin meta information:
__dist__ = dict(
    #The name of your plugin:
    name = "Blog",
    #The namespace of your plugin as used in _config.py.
    #referenced as bf.config.plugins.name
    config_name = "blog",
    #Your name:
    author = "Ryan McGuire",
    #The version number:
    version = "0.8",
    #The URL for the plugin (where to download, documentation etc):
    url = "http://www.blogofile.com",
    #The description of your plugin presented to other Blogofile users:
    description = "A simple blog engine",
    #PyPI description, could be the same, except this text
    #should mention the fact that this is a Blogofile plugin
    #because non-Blogofile users will see this text:
    pypi_description = "A simple blog engine plugin for Blogofile"
    )

__version__ = __dist__["version"]

config = HC(
    # name -- Your Blog's name.
    # This is used repeatedly in default blog templates
    name = "Your Blog's name",
    ## blog_description -- A short one line description of the blog
    # used in the RSS/Atom feeds.
    description = "Your Blog's short description",
    ## blog_path -- Blog path.
    #  This is the path of the blog relative to the site_url.
    #  If your site_url is "http://www.yoursite.com/~ryan"
    #  and you set blog_path to "/blog" your full blog URL would be
    #  "http://www.yoursite.com/~ryan/blog"
    #  Leave blank "" to set to the root of site_url
    path = "/blog",
    ## blog_timezone -- the timezone that you normally write your blog posts from
    timezone = "US/Eastern",
    ## blog_posts_per_page -- Blog posts per page
    posts_per_page = 5,
    # Automatic Permalink
    # (If permalink is not defined in post article, it's generated
    #  automatically based on the following format:)
    # Available string replacements:
    # :year, :month, :day -> post's date
    # :title              -> post's title
    # :uuid               -> sha hash based on title
    # :filename           -> article's filename without suffix
    # path is relative to site_url
    auto_permalink = HC(enabled=True,
                         path=":blog_path/:year/:month/:day/:title"),
    #### Disqus.com comment integration ####
    disqus = HC(enabled=False,
                 name="your_disqus_name"),
    #### Custom blog index ####
    # If you want to create your own index page at your blog root
    # turn this on. Otherwise blogofile assumes you want the
    # first X posts displayed instead
    custom_index = False,
    #### Post excerpts ####
    # If you want to generate excerpts of your posts in addition to the
    # full post content turn this feature on
    #Also, if you don't like the way the post excerpt is generated
    #You can define assign a new function to blog.post_excerpts.method
    #This method must accept the following arguments: (content, num_words)
    post_excerpts = HC(enabled=True,
                        word_length=25),
    #### Blog pagination directory ####
    # blogofile places extra pages of your blog in
    # a secondary directory like the following:
        # http://www.yourblog.com/blog_root/page/4
    # You can rename the "page" part here:
    pagination_dir = "page",
    #### Blog category directory ####
    # blogofile places extra pages of your or categories in
    # a secondary directory like the following:
    # http://www.yourblog.com/blog_root/category/your-topic/4
    # You can rename the "category" part here:
    category_dir = "category",
    priority = 90.0,
    base_template = "site.mako",
    template_path = "_templates/blog",
    #Posts
    post = HC(
        date_format = "%Y/%m/%d %H:%M:%S",
        encoding = "utf-8",
        #### Default post filters ####
        # If a post does not specify a filter chain, use the
        # following defaults based on the post file extension:
        default_filters = {
           "markdown": "syntax_highlight, markdown",
           "textile": "syntax_highlight, textile",
           "org": "syntax_highlight, org",
           "rst": "syntax_highlight, rst",
           "html": "syntax_highlight"
           }
        )
    )

tools = blogofile.plugin.PluginTools(__name__)

def init():
    tools.initialize_controllers()

def run():
    tools.run_controllers()