# Repositório de código das aulas

a nossa google drive - mas mais gira e irritante


# Set-up git and github

So, this might seem like an unnecessary burden, but stick with it! - will make our lives easier in the end, and you'll learn something every programmer uses (...or so they say)!

The idea of _this_ is for you to download the code that I'll place here, and that eventually you can also _push_ your own code, such that I can look at it.

<details>
<summary>info</summary>
<br>
<ul>
<li>
    <strong>git</strong> is what is called a <em>version control system</em>: <em>i.e.</em>, (a fancy name for) a tool that keeps track of your files' history/<em>versions</em> (if you so tell it to...);
</li>
<li>
    furthermore, <strong>git</strong> is also the name of the command that you will run on your terminal for asking it to do stuff
</li>
<li>
    the point is not that this functionality is so important to our purposes (but it might aswell be!); instead, it is what we need for using github - enter:
</li>
<li>
    <strong>github</strong> is, as the name implies, a <em>hub</em> for <strong>git</strong>, <em>i.e.</em>, it is an online center of files (and their versions), specifically <em>code-files</em>;
</li>
<li>
    being online, it can be accessed by anyone and anywhere (much like <em>google drive</em>, but for <em>lighter</em> files), and has specifc functionality for having many people editing the _same_ files - that's the whole point!
</li>
<li>
    in this sense, <strong>github</strong> is basically a collection of <strong>repositories</strong>: each person can have theirs, and decide to share them with other people.
</li>
<li>
    a <strong>repository</strong> is basically a directory - with files and other sub-directories in it - as one has on its personal computer (or, for that matter, on google drive).
</li>
</ul>

</details><br>


## Assumptions

I am assuming you already have a `https://www.github.com` account.

<br>

## Install `git` on your PC

Just download the installer [here](https://git-scm.com/downloads), and run by clicking the thing [as an _executable_].

In order to check whether it is installed, open a _terminal_ (MAC) or _Git-Bash_ (Windows) (it should be installed if you installed `Git`), and  run 
```bash
git --version
```
if it prints something like `git version 2.38.0`, you're good to go! (otherwise tell me)

<br>

## Set `git` user configuration

These will be your `github` information: the user name and the email address you've specified.

Just go again to the _terminal_ and run (substituting your credentials):
```
git config --global user.name YOUR_USER_NAME
```
```
git config --global user.email YOUR_USER_EMAIL
```

You can confirm they are both set by running
```
git config user.name; git config user.email
```
and by seeing what you specified on the console (hopefully!)

<br>

## Connect your local `git` to your `github` automatically

The connection is made via a comunication protocol called _SSH_ (which is _cryptographically safe_ - meaning, it is hard enough for someone else to intercept/read the communication [between you and `github`, in our case] - so everyone uses it, `github` included).  The reason I mention this is that we're going to use it.


<details open>
<summary>[useless] info</summary>
<br>
SSH is based on a system of public and private keys.

The idea behind it is that 
+ person A shares her public key, and keeps the private one to herself (...as the names would suggest!); 
+ then, anyone with the public key (say, person B) can encrypt their messages with it - such as putting them on a small safe - and in such a way that only someone with the private key can decrypt (and thus read -) them.

In our context, you are basically going to 
+ first, _generate_ both of these keys (private and public);
+ second, provide the public key to <strong>github</strong> (you, holding the private one, can <em>decrypted</em> the messages that github is trying to send (only to you) - <em>encrypted</em> with the public key you've given them for that effect!).

(This encrypting/decrypting system is considered safe by making use of some very fun theorems on number theory and complexity theory - also some probability and information theory.)

enough context!
</details> 
<br>


Now, every operating system nowadays comes with an `ssh` module (a function that you can run on the command line [a.k.a. terminal], such as `git`, except it comes _built in_ - no need to install) to perform some encryption-related operations that are widely used; so yours should have it.

You'll use that and then complete the procedure at your `github.com` user page. It is straight-forward enough.


### Generate `ssh` keys

First, you need to generate your `ssh` _keys_: go again to your terminal and run (substituting your user email)

```
ssh-keygen -C YOUR_USER_EMAIL
```

If everything goes ok, it should prompt you with some
```
Generating public/private rsa key pair.
Enter file in which to save the key ([...]/.ssh/id_rsa):
```
at that point you just press ENTER, to proceed.

Then they'll prompt you with some

```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again:
```
at that point, yet again, just press ENTER without writing any passphrase - no need.

If it all goes well, as it should, you'll finally be prompted with some funny-looking art-work. - it's some function of your key (which is a very big number, veeeeery probably a prime one - well).

Now, in order to check what you've got, look inside the directory they have created with that command you've just ran - by running

```
ls ~/.ssh
```
<details><summary></summary>
<strong>ls</strong> lists the contents of the directory, which is name `.ssh`, and is located in your home directory, called `~` in the terminal
</details><br>

inside you should see at least the files
```
id_rsa id_rsa.pub
```
the first being a file with the private key - the second, a file with the public one.

### Add `ssh` agent to `git` (whatever that means)

Then you have to add an agent that I honestly don't know the purpose of, but just run

```
eval $(ssh-agent -s)
```

in order to check that the agent is alive and well - by verifying you get prompted something like

```
Agent pid SOME_NUMBER
```
and then run

```
ssh-add ~/.ssh/id_rsa
```
for them to reference your private key @'somewhere important'. 

### Lend _public_ key to `github`
Now the final step: you just have to save the public one (named `id_rsa.pub`) to `github.com`.

I could write the steps, but I think you're better off following this [link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account). Note that you must substitute their references to `id_ed25519.pub` by your public key: `id_rsa.pub`. Note also that it is the contents of the file that matter (and they want), not the name!

After that, the proper set-up is done!

# Download the whole repository for the first time

Also known as _cloning_ the repository into your computer. Now that you are properly set-up, you just need to actually download the files on the repository (these can be replicated for any other repository on github!, including your own)

The basic idea is that you are going to connect this repository with a directory on your computer (_i.e._, make them the same for now; and also know of each other - such as to keep up with any further changes). Then, as I have this repository also connected to a directory on my computer, we can keep our directories synchronized! - and voila, the purpose.

## Clone repository

So, in order to do that, you just have to go back to the terminal, move to a directory where you want to place this one (you can open a new terminal directly on Finder, or move around within the terminal by running `cd DIRECTORY`, for <strong>c</strong>hanging to that <strong>d</strong>irectory, `ls`, to <strong>l</strong>i<strong>s</strong>t what's in the directory you are currently in, and `pwd`, to get the <strong>p</strong>ath to the <strong>w</strong>orking <strong>d</strong>irectory - the one you're in).

Then run

```
git clone git@github.com:emanuelfrazao/aulas-python.git
```

You should immediatly see a message saying

```
Cloning into 'aulas-python'...
```
and then some stuff ending with `done.`. At this point, they will have created for you a directory named `aulas-python`, with all of the files (and directories structure) of this repository.

And that's it! - hopefully! (tell me whether you managed!)

Then we'll discuss how to add _new stuff_: how you can put things on `github` such that I can download them, and vice-versa. No more cloning! - now it will be called _pulling_.


# Download and add new stuff from/to repository

Also known as _pull_.

TODO

## Download/Pull my new files and changes

## Add/Push your new files and changes (for me to see)






