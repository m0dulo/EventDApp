<template>
  <div>
    <h1>Event List</h1>
    <ul>
      <li v-for="event in events" :key="event.id">
        <router-link :to="'/events/' + event.id">{{ event.name }}</router-link>
        <button @click="buyTicket(event.id)">Buy Ticket</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      events: [
        { id: 1, name: 'Event 1', description: 'Description for Event 1', tickets: 100 },
        { id: 2, name: 'Event 2', description: 'Description for Event 2', tickets: 50 },
        { id: 3, name: 'Event 3', description: 'Description for Event 3', tickets: 200 },
      ],
    };
  },
  methods: {
    buyTicket(eventId) {
      // Implement logic to navigate to the ticket purchase page
      this.$router.push({ path: `/events/${eventId}/purchase` });
    },
  },
};
</script>

