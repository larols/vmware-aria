set_multiple_policies:   
  lgpo.set:     
    - computer_policy:         
        Account lockout duration: 120
        Account lockout threshold: 10
        Reset account lockout counter after: 120
        Maximum password age: 60
        Minimum password length: 7

update_gpo:   
  cmd.run:     
    - name: "gpupdate /force"