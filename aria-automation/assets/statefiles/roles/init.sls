install_multiple_roles:
  win_servermanager.installed:
    - recurse: True
    - name: Web-Server
    - name: Print-Services

install_multiple_features:
  win_servermanager.installed:
    - recurse: True
    - features:
      - BitLocker
      - BitLocker-NetworkUnlock
      - NFS-Client