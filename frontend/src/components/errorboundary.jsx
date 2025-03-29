class ErrorBoundary extends React.Component {
    state = { hasError: false };

    static getDerivedStateFromError(error) {
        return { hasError: true };
    }

    componentDidCatch(error, errorInfo) {
        console.error("Error caught:", error, errorInfo);
    }

    render() {
        return this.state.hasError ? (
            <div>Something went wrong. Please try again.</div>
        ) : this.props.children;
    }
}

<ErrorBoundary>
    <CartPage />
</ErrorBoundary>