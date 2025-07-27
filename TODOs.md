1. Entry for all creatures
    - name
        - string
    - type
        - string
    - location
        - string or array?
    - hp
        - int
    - stealables
        - array
    - drops
        - array
    - amount_caught
    - pre_req
        - desc: need to catch <amount> <name> to unlock <monster> in the Monster Arena


2. Create seed file
3. API to retrieve all creatures
4. Add filter support
    - location*
    - type
    - stealables (?)
    - drops (?)
5. Create UI
    - Base table to display 10-25(?)
        - name, location, amount_caught
    - Ability to filter results
    - Ability to update columns?
        - how to store preference?
 