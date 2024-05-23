export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let total = 0;
  if (weakMap.get(endpoint)) total = weakMap.get(endpoint);
  weakMap.set(endpoint, total + 1);
  if (total + 1 >= 5) throw new Error('Endpoint load is high');
}
