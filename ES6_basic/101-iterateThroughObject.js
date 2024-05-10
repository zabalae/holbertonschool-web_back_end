export default function iterateThroughObject(reportWithIterator) {
  const arr = [];
  for (const r of reportWithIterator) {
    arr.push(r);
  }

  return arr.join(' | ');
}
