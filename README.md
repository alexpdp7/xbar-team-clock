# xbar-team-clock

A quick xbar/Argos plugin to show a customizable world clock in your title bar.
I have only tested this with Argos (for Gnome Shell).

![Screenshot using Argos on Gnome Shell](argos_screenshot.png)

## Requirements

* Python 3
* A suitable extension like:
  * https://github.com/p-e-w/argos
    * Fedora 38: At the time of writing this, [the package on Fedora 38 is broken](https://bugzilla.redhat.com/show_bug.cgi?id=2211941). Until the package is updated, following [the manual installation steps](https://github.com/p-e-w/argos#manually) and using the `e2d68ea23eed081fccaec06c384e2c5d2acb5b6b` commit works.
* Probably Gnu CoreUtils or something, so `TZ=xxx date +"%A %H:%M"` works. I would prefer to use native Python for portability, but I think that would require `zoneinfo`, added in Python 3.9.

## Usage

Create a file called `clock.1m.sh` with contents like: 
 
```
#!/path/to/xbar-team-clock/team-clock.py
Steve;America/Los_Angeles
Nick;America/Denver
Heider;America/Sao_Paulo
Pedro;Europe/Madrid
```

* The first line is a shebang pointing to the `team-clock.py` script
* Every other non-blank line is a clock you want, using the format `text;tz`, where `text` is the text you want to display, and `tz` is the time zone.
* Lines starting with `#` are ignored

Make the file executable and drop it in `~/.config/argos/` (for Argos).
