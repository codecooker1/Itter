import { ref } from 'vue';

export const useHostname = () => {
  const hostnameRef = ref(import.meta.env.VITE_HOSTNAME); 

  const hostname = hostnameRef.value;
  console.log(`hostname is \n ${hostname} (from useHostname)`)
  return { hostname };
};