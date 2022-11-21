disable_print_spooler:
  service.disabled:
    - name: Spooler

stop_print_spooler:
  service.dead:
    - name: Spooler
    
disable_win_telemetry:
  service.disabled:
    - name: DiagTrack

stop_win_telemetry:
  service.dead:
    - name: DiagTrack