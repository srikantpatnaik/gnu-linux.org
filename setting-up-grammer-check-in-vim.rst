How to set grammar check in vim
===============================

Have you ever used web based grammar tool? There are plenty, they help you
learn from your mistakes.

Being a vim user, I couldn't resist myself to explore various such tools for my
life. Sadly, there were few. In fact, only worth mentioning, `LanguageTool
<https://www.languagetool.org/>`_.

Thanks to ``Dominique``, for the vim plugin ``LanguageTool`` (confused?, same
name!), the setup is trivial and straightforward.

Download latest versions of both plugin and tool from following links :

1. The LanguageTool plugin : http://www.vim.org/scripts/script.php?script_id=3223

#. The LanguageTool (stand alone for the desktop) : https://www.languagetool.org/


Extract the plugin into your ``~/.vim`` directory (create if doesn't exist) ::

	cd ~/.vim
	unzip /tmp/LanguageTool.zip

Now generate tags ::

    vim -c 'helptags ~/.vim/doc'

Now extract the LanguageTool(mine was version 3.1) to a known location ::

	unzip /tmp/LanguageTool-3.1.zip -d /opt

Now open your ``~/.vimrc`` and add the path for java command line tool to work
with the plugin ::

	let g:languagetool_jar='/opt/LanguageTool-3.1/languagetool-commandline.jar'


You may now start the vim and test your installation ::

	:help LanguageTool

To invoke grammar check for any content, just invoke(it will take a while to
load) ::

	:LanguageToolCheck

To close the split window, simply issue ::

	:LanguageToolClear

That's all!
I hope to see more development in this project.



