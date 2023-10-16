<template>
  <div>
    <h1>Ticket Purchase</h1>
    <p>Event Name: {{ event.name }}</p>
    <p>Available Tickets: {{ event.tickets }}</p>
    <form @submit.prevent="purchaseTicket">
      <label for="quantity">Quantity:</label>
      <input type="number" id="quantity" v-model="ticketQuantity" />
      <button type="submit">Purchase</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ticketQuantity: 1,
    };
  },
  computed: {
    totalPrice() {
      return this.ticketQuantity * this.ticketPrice;
    },
  },
  methods: {
    purchaseTicket() {
      // Implement logic to handle ticket purchase, update available tickets, etc.
      // You'll also need to implement a backend API for this functionality.
      // For simplicity, we'll just reduce the available tickets here.
      this.event.tickets -= this.ticketQuantity;

      // Redirect to the event details page
      this.$router.push({ path: `/events/${this.event.id}` });
    },
  },
};
</script>
