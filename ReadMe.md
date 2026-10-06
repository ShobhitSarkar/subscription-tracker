# subscription-tracker 

Simple web app to keep track of subscriptions & upcoming payments 

# Requirements 

## Functional Requirements 

- create a subscription 
    - name 
    - frequency 
    - dolllars (total)
    - dollars per month 
- update subscription details 
- delete a subscription from total subscriptions
- dashboard showing all the subscriptions that you paid for this month 
- notification for subscription coming up in the next week 

## Non Functional Requirement 

- Add notes to subscriptions maybe?? 

# Endpoints 

## `subscription/create` 

creates a subscription 

**body:**

```
name 
amount 
frequency
```

## `subscription/update` 

- update the different fields of the notifications object 

## `subscription/delete` 

- deletes the name of the subscription 
- input - subscription name / id 
- returns bool true for sucess, false otherwise 

## `subscription/notification`

- sent out 7 days before deduction 