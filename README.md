## podman-quadlet-ironhide

Repository with [Podman Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html) Systemd unit files running on my home server (which I named Ironhide). The files herein are what is in the Ironhide's `/etc/containers/systemd` directory. Once dropped into the directory, a Systemd daemon reload followed by a service restart is required for changes to take effect.

```
systemctl daemon-reload
```

The env directory in this repository is a Git submodule to a private repository. I have done this as most of the env files contain secrets.

Copy with care; Some hardcoded mounted paths in some of the unit files (e.g. `/mnt/md0`) are expected to be present on the host.
