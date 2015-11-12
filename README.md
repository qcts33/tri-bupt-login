# tri-bupt-login
A python script for BUPT login

---

## Dependent library:

1. [Requests](http://docs.python-requests.org/en/latest/)

## Usage

You can either directly use this script or pack your username and password
pairs into profiles and put them in one configuration file, which useually
`~/.tri_bupt_login.json` or `~/.dot/tri_config.json`.

# Directly login

- Execute the command:

```
login.py [in|out]
```

- Enter your username and password when the prompt pop up.

# Usage accompany with configuration file

- Create a configuration file either located at `~/.tri_bupt_login.json` or
  `~/.dot/tri_config.json`.

- Add contents as below, if you want this script to corporate with other _tri_
  series script, please merge the content according to the json format.

```
{
	"Applications": {
		"tri-bupt-login": {
			"default": {
				"username": "xxxxxxx",
				"password": "*******"
			},
			"profile1": {
				"username": "xxxxxxx",
				"password": "*******"
			}
		}
	}
}
```
- Execute the command, if you do not designate any configuration profile, the
  `default` profile will be invoked. Similarly, if there is no `default` profile,
  a message will be reported.
```
login.py [in|out] [profile_name]
```

# License
![CC License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)
