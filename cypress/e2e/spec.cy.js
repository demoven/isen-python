// describe('Create and connect to an account', () => {
//   it('Visits the Oc commerce site', () => {
//     cy.visit('/home')

//     // User is able to create an account an to be redirect to login pages

//     cy.contains('SIGNUP').click()
//     cy.url().should('include', '/user/signup')
//     // cy.contains('fname')
//     cy.get('[id^=fname]').type('fakeuser')
//     cy.get('[id^=lname]').type('toto')
//     cy.get('[id^=username]').type('fakeuser')
//     cy.get('[id^=email]').type('fake@email.com')
//     cy.get('[id^=pass]').type('1hstesh<23456789')
//     cy.get('[id^=re_pass]').type('1hstesh<23456789')
//     cy.get('form').contains('Register').click()
//     cy.url().should('include', '/user/login')

//     // User is able to connect with the previously created account
//     cy.get('[id^=your_name]').type('fakeuser')
//     cy.get('[id^=your_pass]').type('1hstesh<23456789')
//     cy.get('form').contains('Log in').click()
//     cy.url().should('include', '/home')
//     cy.contains('FAVOURITE')
//   })
// })

describe('Put item in favourite', () => {
  it('Connect to OC commerce and put in favourite', () => {

    // In this test you should load the home url and connect with the previous account
    cy.visit('/home')
    cy.contains('LOGIN').click()
    cy.get('[id^=your_name]').type('fakeuser')
    cy.get('[id^=your_pass]').type('1hstesh<23456789')
    cy.get('form').contains('Log in').click()
    cy.url().should('include', '/home')

    // You will go to favourite pages to make sure there is no favourite
    cy.contains('FAVOURITE').click()

    // Then go back to home
    cy.visit('/home')

    // You will add an item to favourite
    //Hover the product and click on the heart icon
    cy.get('.portfolio-item').first().trigger('mouseover')
    cy.get('.portfolio-item').first().find('.fa-heart').click()

    // You will go to favourite pages to confirm item is here
    cy.contains('FAVOURITE').click()

    // You will then delete the item an check it has been successfully deleted
    cy.get('.table').find('tbody').find('tr').find('td').last().click()

    
  })
})