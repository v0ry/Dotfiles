# coding: utf8

shortcuts = {
    "Vim":{ #https://vim.rtorr.com/
        "open help for keyword":":help keyword",
        "open file":":o file",
        "save file as":":saveas file",
        "close current pane":":close",
        "open man page for word under the cursor":"K",
        "move cursor left":"h",
        "move cursor down":"j",
        "move cursor up":"k",
        "move cursor right":"l",
        "move to top of screen":"H",
        "move to middle of screen":"M",
        "move to bottom of screen":"L",
        "jump forwards to the start of a word":"w",
        "jump forwards to the start of a word (words can contain punctuation)":"W",
        "jump forwards to the end of a word":"e",
        "jump forwards to the end of a word (words can contain punctuation)":"E",
        "jump backwards to the start of a word":"b",
        "jump backwards to the start of a word (words can contain punctuation)":"B",
        "move to matching character (default supported pairs: '()', '{}', '[]')":"%",
        "jump to the start of the line":"0",
        "jump to the first non-blank character of the line":"^",
        "jump to the end of the line":"$",
        "jump to the end of the line":"$",
        "jump to the last non-blank character of the line":"g_",
        "go to the first line of the document":"gg",
        "go to the last line of the document":"G",
        "go to line 5":"5G",
        "jump to next occurrence of character x":"fx",
        "jump to before next occurrence of character x":"tx",
        "jump to previous occurence of character x":"Fx",
        "jump to after previous occurence of character x":"Tx",
        "repeat previous f, t, F or T movement":";",
        "repeat previous f, t, F or T movement, backwards":",",
        "jump to next paragraph (or function/block, when editing code)":"}",
        "jump to previous paragraph (or function/block, when editing code)":"{",
        "center cursor on screen":"zz",
        "move back one full screen":"⌃b",
        "move forward one full screen":"⌃f",
        "move forward 1/2 a screen":"⌃d",
        "move back 1/2 a screen":"⌃u",
        "insert before the cursor":"i",
        "insert at the beginning of the line":"I",
        "insert (append) after the cursor":"a",
        "insert (append) at the end of the line":"A",
        "append (open) a new line below the current line":"o",
        "append (open) a new line above the current line":"O",
        "insert (append) at the end of the word":"ea",
        "exit insert/visual mode":"Esc",
        "replace a single character":"r",
        "join line below to the current one":"J",
        "change (replace) entire line":"cc",
        "change (replace) to the end of the word":"cw",
        "change (replace) to the end of the line":"c$",
        "delete character and substitute text":"s",
        "delete line and substitute text (same as cc)":"S",
        "transpose two letters (delete and paste)":"xp",
        "undo":"u",
        "redo":"⌃r",
        "repeat last command":".",
        #Marking text (visual mode) stopped at
        "start visual mode, mark lines, then do a command (like y-yank)":"v",
        "start linewise visual mode":"V",
        "visual - move to other end of marked area":"o",
        "start visual block mode":"^v",
        "visual - move to other corner of block":"O",
        "visual - mark a word":"aw",
        "visual - a block with ()":"ab",
        "visual - inner block with ()":"ib",
        "visual - inner block with {}":"iB",
        "shift text right":">",
        "shift text left":"<",
        "yank (copy) marked text":"y",
        "delete marked text":"d",
        "switch case":"~",
        "show registers content":":reg",
        "yank into register x":"\"xy",
        "paste contents of register x":"\"xp",
        "list of marks":":marks",
        "set current position for mark A":"ma",
        "jump to position of mark A":"'a",
        "yank text to position of mark A":"y`a",
        "record macro a":"qa",
        "stop recording macro":"q",
        "run macro a":"@a",
        "rerun last run macro":"@@",
        "yank (copy) a line":"yy",
        "yank (copy) 2 lines":"2yy",
        "yank (copy) the characters of the word from the cursor position to the start of the next word":"yw",
        "yank (copy) to end of line":"y$",
        "put (paste) the clipboard after cursor":"p",
        "put (paste) before cursor":"P",
        "delete (cut) a line":"dd",
        "delete (cut) 2 lines":"2dd",
        "delete (cut) the characters of the word from the cursor position to the start of the next word":"dw",
        "delete (cut) to the end of the line":"D",
        "delete (cut) to the end of the line":"d$",
        "delete (cut) character":"x",
        "write (save) the file, but don't exit":":w",
        "write out the current file using sudo":":w !sudo tee %",
        "write (save) and quit":":wq or :x or ZZ",
        "quit (fails if there are unsaved changes)":":q",
        "quit and throw away unsaved changes":":q! or ZQ",
        "write (save) and quit on all tabs":":wqa",
        "search for pattern in multiple files":":vimgrep /pattern/ {file}",
        "search - jump to the next match":":cn",
        "search - jump to the previous match":":cp",
        "search - open a window containing the list of matches":":copen",
        "edit a file in a new buffer":":e file",
        "go to the next buffer":":bnext or :bn",
        "go to the previous buffer":":bprev or :bp",
        "delete a buffer (close a file)":":bd",
        "list all open buffers":":ls",
        "open a file in a new buffer and split window":":sp file",
        "open a file in a new buffer and vertically split window":":vsp file",
        "split window":"Ctrl + ws",
        "switch windows":"Ctrl + ww",
        "quit a window":"Ctrl + wq",
        "split window vertically":"Ctrl + wv",
        "move cursor to the left window (vertical split)":"Ctrl + wh",
        "move cursor to the right window (vertical split)":"Ctrl + wl",
        "move cursor to the window below (horizontal split)":"Ctrl + wj",
        "move cursor to the window above (horizontal split)":"Ctrl + wk",
        "open a file in a new tab":":tabnew or :tabnew file",
        "move the current split window into its own tab":"Ctrl + wT",
        "move to the next tab":"gt or :tabnext or :tabn",
        "move to the previous tab":"gT or :tabprev or :tabp",
        "move to tab number #":"#gt",
        "move current tab to the #th position (indexed from 0)":":tabmove #",
        "close the current tab and all its windows":":tabclose or :tabc",
        "close all tabs except for the current one":":tabonly or :tabo",
        "command - run the command on all tabs (e.g. :tabdo q - closes all opened tabs)":":tabdo"
    }
}