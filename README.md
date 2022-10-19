# Repositório de código das aulas

## 1. Setup (this/any) repository

So, this might seem like an unnecessary burden, but stick with it! - will make our lives easier in the end, and you'll learn something every programmer uses!

The idea of _this_ is for you to download the code that I'll place here, and that eventually you can also _push_ your own code, such that I can look at it.

<details>
<summary>( just a bit of context )</summary>
<br>
`git` is what is called a `version control system`
 

</details><br>


### **1.0. Assumptions**

I am assuming you already have a `github.com` account.



### **1.1. Install `git` on your PC**

Just download it [here](https://git-scm.com/downloads) and run the executable file that you've downloaded.

In order to check whether it is installed, open a _terminal_ (MAC) or _Git-Bash_ (Windows) (it should be installed if you installed `Git`), and  run 
```bash
git --version
```
if it prints something like `git version 2.38.0`, you're good to go! (otherwise tell me)

### **1.2. Set `git` user configurations**

These will be your `github` information: the user name and the email address you've specified.

Just go again to the _terminal_ and run:
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


3. **Connect your local `git` to your `github` automatically**

The connection is made via a comunication protocol called _SSH_ (which is _cryptographically safe_ - meaning, it is hard enough for someone else to interrupt your communication [with `github`, in our case] - so everyone uses it, `github` included) based on a system of public and private keys. 


<details open>
<summary>( just a bit of [useless] context )</summary>
<br>
the idea behind it is that you share your public key, and keep the private one to yourself - as the names would suggest! -; then anyone with the public key can encode their messages with it - such as putting them on a small safe - that only someone with the private key can open
</details> 
<br>


Now, every operating system nowadays comes with an ssh module (a function that you can run on the command line, such as git, except it comes _built in_) to perform certain operations; so yours should have it.

You'll use that and then complete the procedure at your github.com user page. It may sound weird, but it is straightforward enough.




### Step 1

Having git running, 
