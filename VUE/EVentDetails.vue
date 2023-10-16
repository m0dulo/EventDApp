<template>
  <div>
    <h1>Event Details</h1>
    <p>Name: {{ event.name }}</p>
    <p>Description: {{ event.description }}</p>
    <p>Tickets Available: {{ event.tickets }}</p>
    <button @click="buyTicket">Buy Ticket</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      event: null,
    };
  },
  created() {
    // Fetch event details based on the route parameter
    const eventId = this.$route.params.id;
    this.event = this.events.find((e) => e.id === Number(eventId));
  },
  methods: {
    buyTicket() {
      // Implement logic to navigate to the ticket purchase page
      this.$router.push({ path: `/events/${this.event.id}/purchase` });
    },
  },
};
</script>
