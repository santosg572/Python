Introduction
============

This tutorial will help you quickly get up to speed and build mainstream desktop graphical user interfaces with Tk 8.5, 
8.6, and beyond.

Tk has been around forever, but visually hadn't kept pace with the look and feel of modern desktop platforms. Tk 
applications had a well-deserved reputation for… well, being extremely ugly and just not fitting in with what users 
expected to see. In fact, the look and feel harks from a time before many people programming today were even born.

That all changed with the release of Tk 8.5 in 2007. This was a milestone release. It made it possible to build 
applications in Tk that looked like they fit in. They followed platform conventions around look and feel. And as user 
interface standards evolved, so did newer versions of Tk.

The downside is that unless you know one or two crucial things, your Tk applications will still look like they were created 
in 1995. It will appear like nothing has changed. Forget fitting in on modern platforms.

Why? Backward compatibility. Unless existing programs make a few simple changes, they won't look any different. (Imagine if 
you just moved into a rustic and quirky historical home. You'd want someone to point out where they've hidden the light 
switches and power outlets, wouldn't you?)

Tk had its heyday in the early 90's, well before Tk 8.5. Much of the sample code and documentation you'll find online comes 
from that time and still uses the "old way" of doing things. If you're building Tk applications today following those 
examples, you're going to find yourself with a decidedly "retro" user interface… and not in a good way.

Tk is actually remarkably easy to learn and use, which is why it became popular and why it's still used today. But having 
so much outdated information out there makes learning Tk more challenging than it should be.

The general state of Tk documentation (outside of the Tcl-oriented reference documentation, which is excellent) is 
unfortunately not at a high point these days. This is particularly true for developers using Tk from languages other than 
Tcl or working on multiple platforms.

This tutorial will show you how you should be using Tk.

If you're new to Tk or creating a new program, this tutorial will ensure you get started the right way. If you've used Tk 
before, it will help you bring your knowledge right up to date. And if you're updating code that may have been written 
years ago, you'll see step-by-step how to bring it into the modern age.

It's also not a reference guide. It's not going to cover everything, just the essentials you need in 95% of applications. 
The rest you can find in reference documentation.

Who this tutorial is for
This tutorial is designed for developers building tools and applications in Tk 8.5, 8.6, and beyond. It focuses on 
mainstream graphical user interfaces, with buttons, lists, checkboxes, rich text editing, 2D graphics, etc. So if you're 
either looking to hack on Tk's internal C code or build the next great 3D immersive game interface, this is probably not 
the material for you.

So this tutorial will, as much as possible, target developers on the three main platforms (Windows, macOS, Linux). It also 
strives to be language-neutral. It covers using Tk from Python, Tcl, Ruby, and Perl. Even if your own language isn't 
included, the chances are you'll still benefit; since all the languages use the same underlying Tk library, there's 
obviously a lot of overlap.

This tutorial also doesn't teach you the underlying programming language (Tcl, Ruby, Perl, Python, etc.), so you should 
have a basic grasp of that already. Similarly, it assumes a basic familiarity with desktop applications in general. While 
you don't have to be a user interface designer, some appreciation of GUI design is always helpful.

Modern best practices
This tutorial is all about building modern user interfaces using the current tools Tk has to offer. It covers the best 
practices you need to accomplish this. And also what you should avoid.

For most tools, you wouldn't think you'd have to say something like that. But for Tk, that's not the case. As mentioned, Tk 
has had a very long evolution (see Tk Backgrounder), and any evolution tends to leave behind a bit of cruft. Couple that 
with how much graphical user interface platforms and standards have evolved in that time. You can see where keeping 
something as large and complex as a GUI library up to date (and backward compatible) may be challenging.

Tk has, for most of its lifetime, gotten a bad rap, to put it mildly. Some of this has been well deserved, most of it not 
so much. Like any GUI tool, you can create absolutely terrible looking and outdated user interfaces with it. It can also be 
used to develop spectacularly good ones given the proper care and attention. When it comes to Tk, most people know about 
the crappy ones. Most of the good ones people don't even know are built in Tk. In this tutorial, we're going to focus on 
what you need to build good user interfaces. Thankfully, this isn't nearly as hard as it used to be before Tk 8.5.

So, to sum up: modern desktop graphical user interfaces, using modern conventions and design sense, using the modern tools 
provided by Tk 8.5 and 8.6.

The downside of backward compatibility
While maintaining backward compatibility makes upgrading to new versions of libraries much easier for software developers, 
it comes at a cost. When it comes to libraries for rapidly evolving domains like user interfaces, it slows migrating to 
newer and better ways of doing things. It leaves existing applications that technically "work" but no longer behave as they 
should from a user perspective.

As you'll see, the changes introduced since Tk 8.5 required some new ways of doing things for developers. That came with 
many benefits, but also meant that certain things that developers had accomplished using existing ways of doing things 
could no longer be supported. Rather than force developers to migrate their code, they chose to support both the old ways 
and new ways. Developers wanting to use the new and improved features migrated to the new ways of doing things. Code using 
the old ways of doing things still worked—and continues to still work today. Even though those old ways produce user 
interfaces that are archaic and out of place on today's platforms.

Unlike in language communities like Python that encourage migrating to newer and better ways of doing things, and are more 
aggressive at deprecating and eventually removing code that implements outdated practices, Tk took a much more "if it ain't 
(technically) broke, don't fix it" approach.

While there are some niche exceptions, there are two big things that Tk developers should mostly avoid in modern 
applications:

non-themed "classic" widgets for buttons, frames, labels, entries, etc.
the "pack" geometry manager
You'll learn about these shortly. And yes, if you see either of these in the examples or documentation you find online, 
that should be a big red flag. What you're seeing is not following modern best practices.

Tk extensions
When it comes to modern best practices, Tk extensions deserve a special word of note. Over the years, developers have 
created all kinds of add-ons to Tk, for example, adding new widgets not available in the core (or at least not at the 
time). Some well-known and quite popular Tk extensions include BLT, Tix, iWidgets, BWidgets; there are many, many others.

Many of these extensions were created decades ago. Because core Tk has always been highly backward compatible, these 
extensions generally keep working with newer versions. However, they rarely reflect current platform conventions or styles. 
They may "work" but can make your application appear extremely dated or out of place. In many cases, the facilities they 
provide have been made obsolete by newer and more modern facilities built into more recent versions of Tk itself.

If you decide to use Tk extensions, it's highly recommended to investigate and review your choices carefully.

The better way forward
As you've seen, Tk gives you many choices… too many. There are at least six different ways to layout widgets on the screen. 
Multiple widgets can be used to accomplish the same thing, and that's before considering any Tk extensions. Tk emphasized 
backward compatibility, which is a double-edged sword. Most of these old and outdated ways of doing things still keep 
working, year after year. That doesn't mean you should keep using some of them.

In this tutorial, we'll often use different ways of doing things than you'd find in other documentation or examples. Often, 
it's because when those were written, the better ways didn't even exist yet. Sometimes, newer documentation parrots the old 
because the writer didn't know any better. (Here's a litmus test for Tk documentation: does it use the archaic pack instead 
of the modern grid?)

If you want to learn and use Tk, all that choice gets in the way. You don't need to know ten different ways to accomplish 
the same thing. You shouldn't need to do all the research, explore all the options, and make a choice yourself. You need to 
know the right way to do things today. That's what this tutorial will give you.

How to use this tutorial
While this tutorial is designed to be read linearly, feel free to jump around as you see fit. We'll often provide links to 
information, whether links to other documentation on this site, such as our "widget roundup" providing usage info on each 
Tk widget, or to external documentation, such as the full reference for a particular command.

The tutorial also lets you select what language (Tcl, Ruby, Perl or Python) to show. You can change this by the "Show:" 
popup menu which is located in the sidebar, near the top right of each page in the tutorial. But it also lets you see how 
Tk is used by all the different languages, which can itself be quite interesting and useful.

You can find a GitHub repository containing many of the larger examples at https://github.com/roseman/tkdocs.

Typographic conventions
As is typically done, code listings, interpreter or shell commands, and responses will be indicated with a fixed-width 
font. When showing an interactive session with the interpreter, what you type will be in bold fixed-width.

When describing procedure or method calls, the literal parts (e.g., the method name) will be in a plain fixed-width font. 
Parameters, where you should fill in the actual value, will add italics, and optional parameters will be surrounded by '?', 
e.g., set variable ?value?.





