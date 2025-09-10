public class Vector {
    private final double x;
    private final double y;

    public Vector() {
        this(0.0, 0.0);
    }

    public Vector(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double dot(Vector v) {
        return this.x * v.x + this.y * v.y;
    }

    public double cross(Vector v) {
        return this.x * v.y - this.y * v.x;
    }

    public double length() {
        return Math.sqrt(x * x + y * y);
    }

    public boolean isPerpendicular(Vector v) {
        return this.dot(v) == 0;
    }

    public boolean isParallel(Vector v) {
        return this.cross(v) == 0;
    }

    public Vector projection(Vector v) {
        double factor = this.dot(v) / (v.length() * v.length());
        return new Vector(factor * v.x, factor * v.y);
    }

    public double component(Vector v) {
        return this.dot(v) / v.length();
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
