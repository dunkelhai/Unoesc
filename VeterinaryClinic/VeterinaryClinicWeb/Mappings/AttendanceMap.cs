using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class AttendanceMap : IEntityTypeConfiguration<Attendance>
    {
        public void Configure(EntityTypeBuilder<Attendance> builder)
        {
            builder.ToTable("Attendance");

            builder.Property(p => p.AttendanceDate)
                .HasColumnType("datetime")
                .IsRequired();

            builder.Property(p => p.Observation)
                .HasColumnType("varchar(200)");

            builder.HasOne(p => p.Animal)
                .WithMany()
                .OnDelete(DeleteBehavior.NoAction);

            builder.HasOne(p => p.Vet)
                .WithMany()
                .OnDelete(DeleteBehavior.NoAction);

            builder.HasOne(p => p.Clinic)
                .WithMany()
                .OnDelete(DeleteBehavior.NoAction);

            builder.HasMany(p => p.Procedures)
                .WithMany(p => p.Attendances);
        }
    }
}
