describe('test filter buttons', () => {
  it('Connect to OC commerce and click on the button', () => {
    cy.visit('/home')
    cy.contains('Trier par prix croissant').click()   
    cy.wait(5000)
    cy.contains('Trier par prix décroissant').click()
    cy.wait(5000)
  })
})