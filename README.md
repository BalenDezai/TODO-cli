[![Build Status](https://travis-ci.com/BalenD/TODO-cli.svg?branch=master)](https://travis-ci.com/BalenD/TODO-cli)
[![codecov](https://codecov.io/gh/BalenD/TODO-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/BalenD/TODO-cli)
<h1 align="center">
  <br>
  TODO-cli
  <br>
</h1>

<p align="center">
  <a href="#about">About</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#config">Configuration</a>
</p>


<h1 style="color:red" align="center" id="#about">About</h1>

This project is about making a console program that will read every "TODO" mark in your file(s), and print out all of them in the terminal so you can begin working on them.

<h1 style="color:red" align="center" id="#install">Install</h1>

Installing the cli is very simple. Simply run the command

```bash
# install
$ pip install commenttodo
```

<h1 style="color:red" align="center" id="#usage">Usage</h1>

## Commands

| Command       | Action                          |
| ------------- |:-------------------------------:|
| -f / -F       | File(s)/Folder(s) name or path  |
| -m / -M       | is folder or not                |
| -e / -E       | Extenionn(s) to look for        |
| -c / -C       | Start new configuration         |
| -v / -V       | Version                         |

## Examples


```bash
# install
$ todo-cli -f "file.py" 
```
Will look inside of the "file.py" in current directory for comments

```bash
# install
$ todo-cli -f "Tests" -m -e .py .cs
```
Will check every .py and .cs file in the Tests folder for comments

```bash
# install
$ todo-cli -f "C:\\Tests" -m -e .py .cs
```
Will check every .py and .cs file in the "Tests" folder path for comments

```bash
# install
$ todo-cli -c
```
will start a new configuration menu

```bash
# install
$ todo-cli -v
```
will show version


```bash
# install
$ todo-cli -e .py
```

<h1 style="color:red" align="center" id="#config">config</h1>