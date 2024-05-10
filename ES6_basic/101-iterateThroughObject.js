export default function iterateThroughObject(reportWithIterator) {
  const arr = [];
  for (const x of reportWithIterator) {
    arr.push(x);
  }

  return arr.join(' | ');
}
