function initSyntax(target) {
    
    function callBack() {
                        var first_line=SyntaxHighlighter.defaults['first-line']
                        $('div.line','td.gutter').each(function(i) {
                            $(this).html("<a href=#>"+(i+first_line)+"</a>");
                        })
                        //<span class="badge badge-warning">4</span>
                        $('div.syntaxhighlighter').css("height","600px")
                        //*/-------------------加注警告信息---------------------------
                        SyntaxHighlighter.config.notifications.msg.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #999 !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #999 !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
                        SyntaxHighlighter.config.notifications.fail.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #333 !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #333 !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
                        SyntaxHighlighter.config.notifications.info.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #3A87AD !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #3A87AD !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
                        SyntaxHighlighter.config.notifications.important.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #B94A48 !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #B94A48 !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
                        SyntaxHighlighter.config.notifications.warning.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #F89406 !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #F89406 !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
                        SyntaxHighlighter.config.notifications.success.forEach(function(i) {
                            var g=$($('div.line','td.gutter')[i-first_line]);
                            var c=$($('div.line','td.code')[i-first_line]);
                            g.css("cssText",'background-color: #468847 !important');
                            $("a",g).css("cssText",'color: #fff !important');
                            c.css("cssText",'background-color: #468847 !important');
                            $('code',c).css("cssText",'color: #fff !important');
                        })
    }
}