export default function Card({ title, children }: { title: string, children: React.ReactNode }) {
  const num = 1
  return (
    <div className="card" style={{
      marginRight: num+'px',
    }}>
      <h2>{title}</h2>
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="lucide lucide-alarm-clock"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2"/><path d="M5 3 2 6"/><path d="m22 6-3-3"/><path d="M6.38 18.7 4 21"/><path d="M17.64 18.67 20 21"/></svg>
      {children}
    </div>
  )
}
