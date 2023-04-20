import React, { useState } from "react";

const ClientOnly = () => {
  const [hasMounted, setHasMounted] = useState(false);
  return <div>ClientOnly</div>;
};

export default ClientOnly;
