const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();

const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvatica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', {style: style});
card.mount('#card_elements');