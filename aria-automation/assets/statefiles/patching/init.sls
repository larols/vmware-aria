# Update the system using the state defaults
update_system:
  wua.uptodate

# Update the drivers
update_drivers:
  wua.uptodate:
    - software: False
    - drivers: True
    - skip_reboot: False

# Apply all critical updates
update_critical:
  wua.uptodate:
    - severities:
      - Critical
      - Important
    - skip_reboot: False